var
  t:text;
  i,x,m,Y:longint;
begin
  assign(t,'a1.in');
  rewrite(t);
  assign(m,'a1.out');
  rewite(m);
  read(t,x);
  while not eof(f) do
   begin
     y:=sqr(x);
     writeln(m,y);
     read(t,x);
   end;
   close(t);
   close(m);
end.
