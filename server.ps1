$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add("http://localhost:8000/")
try {
    $listener.Start()
    Write-Output "Server listening on http://localhost:8000/"
} catch {
    Write-Error "Failed to start listener: $_"
    exit
}

while ($listener.IsListening) {
    try {
        $context = $listener.GetContext()
        $request = $context.Request
        $response = $context.Response
        
        $urlPath = $request.Url.LocalPath
        if ($urlPath -eq "/" -or $urlPath -eq "") {
            $urlPath = "/index.html"
        }
        
        # Build path to the file inside build directory
        $cleanPath = $urlPath.Replace("/", "\").TrimStart('\')
        $filePath = Join-Path "build" $cleanPath
        
        if (Test-Path $filePath -PathType Leaf) {
            $bytes = [System.IO.File]::ReadAllBytes($filePath)
            
            # Set content type
            if ($filePath -like "*.html") { $response.ContentType = "text/html; charset=utf-8" }
            elseif ($filePath -like "*.css") { $response.ContentType = "text/css" }
            elseif ($filePath -like "*.js") { $response.ContentType = "application/javascript" }
            elseif ($filePath -like "*.png") { $response.ContentType = "image/png" }
            elseif ($filePath -like "*.jpg" -or $filePath -like "*.jpeg") { $response.ContentType = "image/jpeg" }
            elseif ($filePath -like "*.webp") { $response.ContentType = "image/webp" }
            elseif ($filePath -like "*.svg") { $response.ContentType = "image/svg+xml" }
            elseif ($filePath -like "*.xml") { $response.ContentType = "application/xml" }
            
            $response.ContentLength64 = $bytes.Length
            $response.OutputStream.Write($bytes, 0, $bytes.Length)
        } else {
            $response.StatusCode = 404
            $errorMessage = "404 Not Found"
            $errBytes = [System.Text.Encoding]::UTF8.GetBytes($errorMessage)
            $response.ContentLength64 = $errBytes.Length
            $response.OutputStream.Write($errBytes, 0, $errBytes.Length)
        }
        $response.OutputStream.Close()
    } catch {
        # Log error and continue listening
        Write-Warning "Request handling failed: $_"
    }
}
