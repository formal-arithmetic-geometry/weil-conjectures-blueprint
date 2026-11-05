+++
id = "example-running-example-trace-formula"
kind = "example"
title = "The running example: the trace formula"
order = 1042
uses = ["example-running-example-duality"]
+++
For the elliptic curve $C_0\colon y^2=x^3-x$ over $\mathbf F_3$,
geometric Frobenius acts on $H^0(C,\mathbf Q_\ell)=\mathbf Q_\ell$ by $1$ and on
$H^2(C,\mathbf Q_\ell)=\mathbf Q_\ell(-1)$ by $3$, and $H^1(C,\mathbf Q_\ell)$ is a plane
(Example [example-running-example-duality]). The point-counting formula reads

$$
N_m=1-\operatorname{Tr}\bigl(F^m\mid H^1(C,\mathbf Q_\ell)\bigr)+3^m .
$$

From $N_1=4$ we get $\operatorname{Tr}(F\mid H^1)=0$. Duality gives
$\det(F\mid H^1)=3$, so $\det(1-TF\mid H^1)=1+3T^2$. Hence

$$
Z(C_0,T)=\frac{1+3T^2}{(1-T)(1-3T)}.
$$

The formula predicts $N_2=1+9+6=16$ and $N_3=1+27-0=28$, and direct
counts over $\mathbf F_9$ and $\mathbf F_{27}$ confirm this. In general, for a
genus-one curve over $\mathbf F_q$ the single number $N_1$ determines
$P_1=1-(1+q-N_1)T+qT^2$, and therefore every $N_m$.
