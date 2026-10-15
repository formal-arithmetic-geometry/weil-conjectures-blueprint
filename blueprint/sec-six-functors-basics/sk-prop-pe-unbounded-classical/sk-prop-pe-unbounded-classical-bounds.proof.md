+++
kind = "proof"
of = "det-pe-unbounded-classical-bounds"
+++
By [det-base-field-cd-finite-field], $\operatorname{cd}_{\rm tor}(k)\leq1$. Let $W$
be a scheme of finite type over $k$ admitting an étale morphism to $X$. Then
$\dim W\leq\dim X$, since étale morphisms have discrete fibres and are
open, and [thm-sc-finite-type-torsion-cd] gives
$\operatorname{cd}_{\rm tor}(W)\leq2\dim X+1=e_X$.

*(1).* Each $U_i$ is affine étale over $X$, hence of finite type over $k$, so
$\operatorname{cd}_{\rm tor}(U_i)\leq e_X$ for all $i$. The scheme $U$ is the limit
of the qcqs schemes $U_i$ along affine transition maps, so
[lem-sc-cd-affine-limit] gives $\operatorname{cd}_{\rm tor}(U)\leq e_X$. The slice
$X_{\Proet}/U$ is $U_{\Proet}$ and $(\nu_X^*G)|_U\cong\nu_U^*(G|_U)$, so the
cohomology comparison ([sk-prop-sf-comparison]) gives
$H^q(U_{\Proet},(\nu_X^*G)|_U)\cong H^q(U_{\Et},G|_U)=0$ for $q>e_X$.

*(2).* Each $V_i$ is affine and étale over $Y$, hence of finite type over $k$, and
$X\times_YV_i$ is of finite type over $k$ and étale over $X$. So
$\operatorname{cd}_{\rm tor}(X\times_YV_i)\leq e_X$. The scheme
$X\times_YV=\varprojlim_iX\times_YV_i$ is a limit of qcqs schemes along affine
transition maps (base changes of the affine maps $V_j\to V_i$), and
[lem-sc-cd-affine-limit] and the cohomology comparison conclude as in (1).

*(3).* The sheaf $R^qg_{\Et,*}G$ is the sheafification of
$V\mapsto H^q((X\times_YV)_{\Et},G)$ on affine étale $V\to Y$. Each
$X\times_YV$ is of finite type over $k$ and étale over $X$, so these groups vanish
for $q>e_X$.

The statements for $Y$ are the case $g=\mathrm{id}_Y$.
