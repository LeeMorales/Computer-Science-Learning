var
  sum:real;
  i:longint;
begin
  sum:=1;
  for i:=1 to 100 do
    sum:=sum*i;
  write(sum);
end.