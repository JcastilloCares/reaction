# Getting Started with Create React App

This project was bootstrapped with [Create React App](https://github.com/facebook/create-react-app).

## Available Scripts

In the project directory to start the app run:

```
npm start
```

This runs the app in the development mode.

Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.

You may also see any lint errors in the console.

# Test

To test first make sure Python is up-to-date and install dependencies

```commandline
pip install pytest playwright
playwright install
```

Then use this command to launch your tests

```commandline
pytest test/
```

Note: if you are running this locally make sure your app is running locally too on http://localhost:3000 as the test uses this