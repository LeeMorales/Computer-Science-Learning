var
  i,s,n,m:longint;
begin
  readln(n);
  for i:=1 to n do
    begin
      read(m);
      s:=s+m;
      writeln(s);
    end;
  writeln(s);
end.