const repl = require('repl');

// custom writer function that outputs nothing
const writer = function(output) {
  // don't output anything
  return '';
};

const startRepl = function(instream, outstream) {
  const options = {
    input: instream,
    output: outstream,
    prompt: '',
    writer: writer
  };
  const r = repl.start(options);

  // custom print function for Notebook interface
  const print = function(data, variable) {
    // bundle the data into an object
    const obj = { _pixiedust: true, type: 'print', data: data, variable: variable };
    outstream.write(JSON.stringify(obj) + '\n')
  };

  // custom display function for Notebook interface
  const display = function(data, variable) {
    // bundle the data into an object
    const obj = { _pixiedust: true, type: 'display', data: data, variable: variable };
    outstream.write(JSON.stringify(obj) + '\n')
  };

  // add silverlining library and print/display
  r.context.silverlining = require('silverlining');
  r.context.request = require('request-promise-native');
  r.context.print = print;
  r.context.display = display;
  return r;
};

startRepl(process.stdin, process.stdout);
console.log("Pixiedust Node started");