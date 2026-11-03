+++
kind  = "proof"
of    = "sk-d-real-weil"
+++
The exact sequence is [lem-wf-weil-group-exact-sequence]. The local
Frobenius $F_x$ is well defined up to conjugacy in $W(U_0)$.
Changing the path conjugates it by some $g\in\pi_1(U_0)$, and this is
already a conjugation inside $W(U_0)$: identify $\Gal(k/\Fq)$ with
$\widehat{\mathbf Z}$ by sending geometric Frobenius to $1$, so that
$\deg$ extends to $\pi_1(U_0)\to\widehat{\mathbf Z}$ with
$W(U_0)=\deg^{-1}(\mathbf Z)$. Since
$\widehat{\mathbf Z}=\mathbf Z+d(x)\widehat{\mathbf Z}$, write
$\deg g=n+d(x)t$ with $n\in\mathbf Z$ and $t\in\widehat{\mathbf Z}$, and
let $F_x^t$ be the image of the $t$-th power of geometric Frobenius in
the procyclic group $\Gal(\overline{\kappa(x)}/\kappa(x))\simeq\widehat{\mathbf Z}$;
it has degree $d(x)t$ and commutes with $F_x$. Then $w=gF_x^{-t}$ has
degree $n$, so $w\in W(U_0)$, and
$gF_xg^{-1}=wF_x^{t}F_xF_x^{-t}w^{-1}=wF_xw^{-1}$. Hence conjugacy in
$\pi_1(U_0)$ and in $W(U_0)$ agree on $F_x$.

The equivalence with representations is
[prop-wf-weil-sheaf-representation-equivalence]: at the geometric level it is
the lisse sheaf–representation equivalence of [sk-p-real-integral] (for smooth
curves also [thm-lisse-qlbar-representations]), and a Weil structure
$\varphi:\Frob^*\mathcal F\to\mathcal F$ is the same as an automorphism
$\Phi$ of the generic stalk with $\Phi\rho(g)\Phi^{-1}=\rho(sgs^{-1})$ for
$g\in P$, which extends $\rho$ to $W(U_0)$ by $\rho(s)=\Phi$.
