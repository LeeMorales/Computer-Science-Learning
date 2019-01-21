var
  n,m,b,i,a,s,d,w:longint;
begin
  for i:=100 to 9999 do
  begin
  n:=i div 100;
  m:=i div 10 mod 10;
  b:=i div 10;
  if ((n<>m)) and ((m<>b)) and (m>(n+b)) then begin
                                                for d:=100 to 9999 do
                                                if a mod d=0 then w:=w+1;
                                                if s=2 then write('yes!')
                                                       else write('no.....');
   write(n,m,b);
                                            end;
  end;
end.
