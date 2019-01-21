var
  a,i:integer;
  b:char;
begin
  writeln('Welcome to program "dictionary",you can look of "ASCLL" dictionary or find ASCLL in this program.If you write "1",program can show the dictionary.If you write "2",program can let you write "ASCLY" and write the charcter for you');
  readln(a);
  if a=1 then
  begin
    for i:=0 to 100 do
    begin
      if i mod 10=1 then
      writeln;
      write(i,':',chr(i),' ');
    end;
  end;
  if a=2 then
  begin
    readln(b);
    writeln(b,':',ord(b),' ');
  end;
end.
