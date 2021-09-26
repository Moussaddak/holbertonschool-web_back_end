process.stdout.write('Welcome to Holberton School, what is your name?\n');
process.stdin.on('readable', () => {
  const input = process.stdin.read();
  if (input) process.stdout.write(`Your name is: ${input}`);
})
  .on('close', () => {
    process.stdout.write('This important software is now closing\n');
  });
