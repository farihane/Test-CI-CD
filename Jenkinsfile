pipeline {
  agent any

  environment {
    MAVEN_VOLUME = 'maven_repo_cache'
  }

  options {
    timestamps()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Detect Java from pom.xml') {
      steps {
        bat '''
          for /f "usebackq tokens=* delims=" %%A in (`powershell -NoProfile -Command ^
            "$xml = [xml](Get-Content pom.xml); ^
             $v = $xml.project.properties.'java.version'; ^
             if (-not $v) { $v = $xml.project.properties.java_version }; ^
             if (-not $v) { $v = $xml.project.properties.java }; ^
             if (-not $v) { $v = $xml.project.properties.'maven.compiler.release' }; ^
             if (-not $v) { $v = $xml.project.build.plugins.plugin.configuration.release }; ^
             if (-not $v) { $v = '21' }; ^
             Write-Output $v"`) do set JAVA_VERSION=%%A
          echo Detected JAVA_VERSION=%JAVA_VERSION%
        '''
        bat '''
          set "MAVEN_IMAGE="
          if "%JAVA_VERSION%"=="21" set MAVEN_IMAGE=maven:3.9.2-eclipse-temurin-21
          if "%JAVA_VERSION%"=="17" set MAVEN_IMAGE=maven:3.9.2-eclipse-temurin-17
          if "%JAVA_VERSION%"=="11" set MAVEN_IMAGE=maven:3.9.2-eclipse-temurin-11
          if not defined MAVEN_IMAGE set MAVEN_IMAGE=maven:3.9.2-eclipse-temurin-21
          echo Using MAVEN_IMAGE=%MAVEN_IMAGE%
          echo MAVEN_IMAGE=%MAVEN_IMAGE%> maven_image.env
        '''
        script {
          def kv = readFile('maven_image.env').trim()
          env.MAVEN_IMAGE = kv.split('=')[1]
        }
      }
    }

    stage('Pull Maven image') {
      steps {
        bat """
          docker pull "%MAVEN_IMAGE%"
        """
      }
    }

    stage('Build (Dockerized Maven)') {
      steps {
        bat """
          docker volume create %MAVEN_VOLUME% 1>nul 2>nul
          docker run --rm ^
            -v "%WORKSPACE%":/app ^
            -v %MAVEN_VOLUME%:/root/.m2 ^
            -w /app ^
            "%MAVEN_IMAGE%" ^
            mvn -B -DskipTests clean package
        """
      }
    }

    stage('Archive JAR') {
      steps {
        archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
      }
    }

    stage('Docker Build App (optional)') {
      when {
        expression { fileExists('Dockerfile') }
      }
      steps {
        bat """
          docker build -t backend-cicd-demo:latest "%WORKSPACE%"
        """
      }
    }
  }

  post {
    success {
      echo '✅ Build réussi'
    }
    failure {
      echo '❌ Build échoué'
    }
    always {
      echo '🧹 Fin du pipeline'
    }
  }
}
