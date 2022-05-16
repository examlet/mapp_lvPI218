from sys import path 
path.append('.')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        "main:app",
        host='127.0.0.1', port=8000,
        reload=True, debug=True, workers=1,
    )