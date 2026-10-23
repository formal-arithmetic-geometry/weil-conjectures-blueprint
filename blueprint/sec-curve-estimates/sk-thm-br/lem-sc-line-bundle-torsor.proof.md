+++
kind  = "proof"
of    = "lem-sc-line-bundle-torsor"
+++
*$\mathcal L_{\Et}$ is a sheaf.* For an etale covering
$\{U_i\to U\}$ of an etale $X$-scheme $U$, the sheaf condition for
$\mathcal L_{\Et}$ is the statement that
$\operatorname{Hom}(\mathcal O_U,\mathcal L_U)=\Gamma(U,\mathcal L_U)$
is computed by compatible families on the $U_i$; an etale covering is
an fpqc covering, so this is the full faithfulness in part 1 of
[lem-pc-fpqc-descent]. The same applies to $\mathcal O_{X_{\Et}}$.

*From modules to torsors.* For invertible $\mathcal L$, the sheaf
$T:=\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L_{\Et})$ is a
$\mathbf G_m$-torsor ([def-sc-gm-torsor]): the action is free
and transitive, and on a trivializing Zariski open $U$ with
$\mathcal L|_U\cong\mathcal O_U$ one has
$T|_U\cong\mathbf G_m|_U$ via $\varphi\mapsto\varphi(1)$.
Moreover the map $[(\varphi,a)]\mapsto\varphi(a)$ is an isomorphism

$$
(T\times\mathcal O_{X_{\Et}})/\mathbf G_m\xrightarrow{\ \sim\ }\mathcal L_{\Et},
$$

well-defined because $g\varphi(g^{-1}a)=\varphi(a)$, and an
isomorphism because it is so on each $U$ above (where it becomes
$(u,a)\mapsto ua$ on $(\mathbf G_m\times\mathcal O_U)/\mathbf G_m$).

*From torsors to modules (descent).* Let $T$ be a
$\mathbf G_m$-torsor, trivialized by sections $t_i\in T(U_i)$ on an
etale covering $\{U_i\to X\}$. On $U_{ij}:=U_i\times_XU_j$ write
$t_j=g_{ij}t_i$ with $g_{ij}\in\Gamma(U_{ij},\mathcal O^{\times})$;
then $g_{ik}=g_{jk}g_{ij}$ on $U_{ijk}$. Multiplication by $g_{ij}$
is a descent datum on the invertible modules $\mathcal O_{U_i}$ for
the fpqc covering $\{U_i\to X\}$ (the cocycle condition is the
displayed identity), so by part 3 of [lem-pc-fpqc-descent] there is
an invertible $\mathcal O_X$-module $\mathcal L(T)$ with
trivializations $e_i\in\Gamma(U_i,\mathcal L(T))$ satisfying
$e_j=g_{ij}e_i$. The map $t_i\mapsto(1\mapsto e_i)$ is compatible on
overlaps, hence glues (as $T$ and the $\underline{\operatorname{Isom}}$
sheaf are sheaves) to a $\mathbf G_m$-equivariant map
$T\to\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L(T)_{\Et})$,
and an equivariant map of $\mathbf G_m$-torsors is an isomorphism
(check locally, where it is a translation of $\mathbf G_m$). By the
previous step $\mathcal L(T)_{\Et}\cong(T\times\mathcal O_{X_{\Et}})/\mathbf G_m$.

*Mutually inverse.* The previous step shows every torsor is
isomorphic to one of the form
$\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L_{\Et})$.
Conversely, if $\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal L_{\Et})\cong
\underline{\operatorname{Isom}}(\mathcal O_{X_{\Et}},\mathcal M_{\Et})$
as torsors, then applying $(-\times\mathcal O_{X_{\Et}})/\mathbf G_m$
and the isomorphism of the second step gives an
$\mathcal O_{X_{\Et}}$-linear isomorphism
$\mathcal L_{\Et}\cong\mathcal M_{\Et}$; evaluating on Zariski opens
$U\subseteq X$ (where $\mathcal L_{\Et}(U)=\mathcal L(U)$) yields
$\mathcal L\cong\mathcal M$. Hence the two constructions are mutually
inverse on isomorphism classes.

*Zariski.* Replacing etale coverings by Zariski open coverings,
$\mathcal L_{\Et}$ by $\mathcal L$ and $\mathbf G_m$ by
$\mathcal O_X^{\times}$, the same argument applies, the descent step
being ordinary gluing of sheaves along an open covering; the second
step identifies the inverse with
$T\mapsto(T\times\mathcal O_X)/\mathcal O_X^{\times}$.
