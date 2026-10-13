+++
id = "sk-d-corr"
kind = "definition"
title = "Correspondences and supported classes"
order = 2619
uses = ["sk-d-setup", "sk-d-six", "sk-thm-sf-comp-composition"]
lean = ["AlgebraicGeometry.ProEtale.Correspondence"]
tags = ["sketch"]
+++
Let $X,Y$ be schemes over $s$, with
$K\in D(X,A)$ and $L\in D(Y,A)$.
A correspondence from $(X,K)$ to $(Y,L)$ consists of a scheme $C$ over $s$,
two $s$-morphisms $c_1:C\to Y$ and $c_2:C\to X$, i.e.
$c=(c_1,c_2):C\to Y\times X$, such that $c_1$ is compactifiable and
$Rc_{1!}$ has a right adjoint $c_1^!$, and a coefficient map
$u:c_2^*K\to c_1^!L$, using the geometric operations.
The ordinary-pullback leg is $c_2$. For an opposite correspondence
$d=(d_1,d_2):D\to X\times Y$, $v:d_2^*L\to d_1^!K$, put

$$
Z=Y\times X,\quad \bar d=\tau d,\quad E(C,D)=C\times_ZD.
$$

Here $\tau$ exchanges factors. For an endocorrespondence,
$F=\Fix(c)=C\times_{X\times X,\,c,\,\Delta_X}X$, the equalizer of $c_1$ and $c_2$.
For $i:T\to Z$, a class supported on $i$ means an element of
$H_T^0(Z,P)=\operatorname{Hom}(Ri_!A_T,P)$.
Tensor–Hom adjunction, the projection formula, and exceptional adjunction
identify such classes with coefficient maps; the supported class $[u]$ is the
inverse image of $u$ under

$$
\operatorname{Hom}\bigl(Rc_!A_C,\RHom_A(p_2^*K,p_1^!L)\bigr)
\simeq\operatorname{Hom}(c_2^*K,c_1^!L),
$$

so it carries the same information as $u$ and is not separate data.
All supports and structure maps remain specified data.
