var
  t:text;
  i:longint;
begin
  assign(t,'a1.dat');
  rewrite(t);
  for i:=1 to 100 do
    begin
      write(t,i);
      write(t,' ');
    end;
   close(t);
end.