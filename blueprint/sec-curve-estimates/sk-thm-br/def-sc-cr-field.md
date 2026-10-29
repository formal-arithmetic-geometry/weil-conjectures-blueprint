+++
id = "def-sc-cr-field"
kind = "definition"
title = "$C_r$ fields"
order = 1435
lean = ["IsCField", "IsQuasiAlgClosed", "IsCField.mono", "IsAlgClosed.isCField_zero"]
+++
Let $r\geq0$. A field $K$ is *$C_r$* if every
homogeneous polynomial form $F\in K[x_1,\dots,x_N]$ of degree
$d>0$ in $N>d^r$ variables has a nontrivial zero in $K^N$, i.e. there is
$x\in K^N$ with $x\neq0$ and $F(x)=0$.

For $r=1$ this reads: every homogeneous form of degree $d$ in $N>d$
variables has a nontrivial zero. If $r\leq s$, then $d^r\leq d^s$, so a
$C_r$ field is $C_s$. For $r=0$ the condition is $N>1$, and an
algebraically closed field is $C_0$: for $F$ of degree $d>0$ in $N\geq2$
variables, $F(x_1,x_2,0,\dots,0)$ is either zero or a binary form of
degree $d$, which is a product of linear forms over an algebraically closed
field; either way it vanishes at some $(x_1,x_2)\neq0$. In particular
$C_0\Rightarrow C_1$.
