var
  x,s:longint;
begin
  x:=1;
  while x<=256 do
  begin
    s:=s+x;
    x:=x*2;
  end;
  write(s);
end.
