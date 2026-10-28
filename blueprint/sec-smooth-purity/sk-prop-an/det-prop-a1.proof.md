+++
kind  = "proof"
of    = "det-prop-a1"
+++
The closed–open pair $(s,j)$ gives the localization triangle
$Rs_*Rs^{!}F\to F\to Rj_*j^*F\xrightarrow{+1}$ on $\Aaf^1_Y$. Apply
$Rp_*$ and use $ps=\mathrm{id}$, so that $Rp_*Rs_*Rs^{!}F=Rs^{!}F$:

$$
Rs^{!}\Lambda(1)\longrightarrow Rp_*\Lambda(1)
\longrightarrow R\pi_*\Lambda(1)\xrightarrow{\ +1\ }.
$$

By [det-prop-a1-kummer] (a) the middle term is $\Lambda_Y(1)$ in degree zero;
by (b) and (c) the right-hand term has $\mathcal H^0=\Lambda_Y(1)$,
$\mathcal H^1=\Lambda_Y\cdot\kappa(t)$ and nothing else. The degree-zero
map is $p^*$, an isomorphism by (b), so the long exact sequence forces
$\mathcal H^m(Rs^{!}\Lambda(1))=0$ for $m\ne2$ and
$\mathcal H^2(Rs^{!}\Lambda(1))\simeq\mathcal H^1(R\pi_*\Lambda(1)) \simeq\Lambda_Y$, the connecting map of the triangle carrying the generator
$\kappa(t)$ of $\mathcal H^1(R\pi_*\Lambda(1))$ to $\partial\kappa(t)$: this
is the isomorphism of sheaves
$\Lambda_Y\xrightarrow{\sim}\mathcal H^0(Rs^{!}\Lambda(1)[2])$,
$1\mapsto\partial\kappa(t)$, of the statement. Thus $Rs^{!}\Lambda(1)[2]$
sits in degree zero with $\mathcal H^0$ constant of rank one. Being
concentrated in degree zero, it has
$\operatorname{Hom}(\Lambda_Y,Rs^{!}\Lambda(1)[2])=\Gamma(Y,\mathcal H^0)$,
and the same triangle on global sections (the long exact sequence
$H^*_{s(Y)}(\Aaf^1_Y,-)\to H^*(\Aaf^1_Y,-)\to H^*(\mathbf G_{m,Y},-)$)
identifies this module with $H^2_{s(Y)}(\Aaf^1_Y,\Lambda(1))$; this is the
separate global statement, and it is an identification of modules, not of
sheaves. Base-change compatibility in [det-prop-a1-kummer] shows that
$\partial\kappa(t)$ restricts to the normalized generator $1$ at every
geometric point. Finally a morphism $\Lambda_Y\to Rs^{!}\Lambda(1)[2]$ is a
global section of the sheaf $\mathcal H^0$, hence determined by its stalks;
so $\mathrm{pur}_s$ is the unique morphism with the stated normalization.
