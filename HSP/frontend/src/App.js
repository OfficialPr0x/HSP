import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import { ThemeProvider } from '@material-ui/core/styles';
import CssBaseline from '@material-ui/core/CssBaseline';
import theme from './theme';
import Header from './components/Header';
import Sidebar from './components/Sidebar';
import Dashboard from './pages/Dashboard';
import PentestGuide from './pages/PentestGuide';
import AIAssistant from './components/AIAssistant';
import ErrorBoundary from './components/ErrorBoundary';

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <ErrorBoundary>
        <Router>
          <div className="app">
            <Header />
            <div className="main-container">
              <Sidebar />
              <main className="content">
                <Switch>
                  <Route exact path="/" component={Dashboard} />
                  <Route path="/guide" component={PentestGuide} />
                </Switch>
              </main>
              <AIAssistant />
            </div>
          </div>
        </Router>
      </ErrorBoundary>
    </ThemeProvider>
  );
}

export default App;