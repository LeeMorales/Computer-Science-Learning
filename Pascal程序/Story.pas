var
  t,s:text;
  a,b,c,d:longint;
  i:array[1..100] of longint;
begin
  assign(t,'story.in');
  reset(t);
  assign(s,'story.out');
  rewrite(t,a);
  for i:=1 to 10 do
    begin
      read(t,a[i]);
      s:=s+a[i];
    end;
   write(y,s);
   close(t);
   close(y);
end.


