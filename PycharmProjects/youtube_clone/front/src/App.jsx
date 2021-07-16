import React from "react";
import { indigo } from "@material-ui/core/colors";
import { createTheme } from "@material-ui/core/styles";
import { ThemeProvider as MuiThemeProvider } from "@material-ui/styles";

import Main from "./components/Main";
import NavBar from "./components/NavBar";
import "./App.css";
import ApiContextProvider from "./context/ApiContext";

const theme = createTheme({
  palette: {
    primary: indigo,
    secondary: {
      main: "#f44336",
    },
  },
  typography: {
    fontFamily: '"Comic Neue",cursive',
  },
});

function App() {
  return (
    <ApiContextProvider>
      <MuiThemeProvider theme={theme}>
        <NavBar />
        <Main />
      </MuiThemeProvider>
    </ApiContextProvider>
  );
}

export default App;
