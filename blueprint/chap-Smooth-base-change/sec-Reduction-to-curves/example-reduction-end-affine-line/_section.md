+++
id = "example-reduction-end-affine-line"
kind = "example"
title = "Where the reduction ends"
order = 684
uses = ["proposition-base-change-larger-algebraically-closed"]
+++
The square of the lemma is itself an instance of smooth base change, and
the simplest case shows what remains to be proved. Let $Y=S=\operatorname{Spec}L$
with $L$ algebraically closed, let $g:Y'=C=\mathbf A^1_L\to Y$ be the
structure map, and take direct image along
$f:X=\operatorname{Spec}\Omega\to Y$ for an algebraically closed extension
$\Omega$ of $L$, so that $X'=\mathbf A^1_\Omega$ and $f'=h$. The sheaf
$R^qf_*\mathbf Z/m$ on $\operatorname{Spec}L$ is
$H^q(\operatorname{Spec}\Omega,\mathbf Z/m)$, which vanishes for $q\geq1$.
So smooth base change for this square says exactly that
$R^qh_*\mathbf Z/m=0$ for $q\geq1$. For $m$ invertible in $L$ this is the
content of
Proposition [proposition-base-change-larger-algebraically-closed] below.

Let $q=1$ and $m$ invertible in $L$. The sections over $C$ itself are no
problem: choosing $\mu_m\simeq\mathbf Z/m$, the Kummer sequence gives
$H^1(\mathbf A^1_\Omega,\mathbf Z/m)=\Omega^*/(\Omega^*)^m=0$, since
$\Gamma(\mathbf A^1_\Omega,\mathcal O)^*=\Omega^*$ is divisible and
$\operatorname{Pic}(\mathbf A^1_\Omega)=0$. However, the presheaf whose
sheafification is $R^1h_*\mathbf Z/m$ has other sections. For example, on
the open $U=\mathbf G_{m,L}$ of $C$ the group
$H^1(\mathbf G_{m,\Omega},\mathbf Z/m)$ is cyclic of order $m$, and such a
class has to be killed by an étale
covering of $U$, as we shall see after the statement of the proposition.

For $m=p$ in characteristic $p$ the argument breaks down already over $C$
itself. Indeed, the group $H^1(\mathbf A^1_\Omega,\mathbf F_p)$ is the
cokernel of $u\mapsto u^p-u$ on $\Omega[x]$, and for $\omega\in\Omega$ transcendental over
$L$ it contains the class of $\omega x$, which does not come from $C$
(compare the class of $tx$ at the beginning of the chapter).
