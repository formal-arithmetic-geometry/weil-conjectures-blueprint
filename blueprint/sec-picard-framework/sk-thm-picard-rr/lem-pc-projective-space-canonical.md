+++
id = "lem-pc-projective-space-canonical"
kind = "lemma"
title = "The canonical sheaf of projective space"
lean = ["AlgebraicGeometry.ProjectiveSpace.nonempty_H_canonicalModule_top_linearEquiv", "AlgebraicGeometry.ProjectiveSpace.isFiniteLocallyFreeOfRank_relativeDifferentials", "AlgebraicGeometry.ProjectiveSpace.canonicalModule", "AlgebraicGeometry.ProjectiveSpace.canonicalGenerator", "AlgebraicGeometry.ProjectiveSpace.isFreeGenerator_canonicalGenerator", "AlgebraicGeometry.ProjectiveSpace.map_canonicalGenerator_eq_transitionUnit_smul", "AlgebraicGeometry.ProjectiveSpace.canonicalModuleIsoTwist", "AlgebraicGeometry.ProjectiveSpace.canonicalModuleIsoTwist_hom_app", "AlgebraicGeometry.ProjectiveSpace.canonicalModuleIsoTwist_hom_app_smul"]
order = 626
uses = ["def-pc-proj", "def-pc-projective-space-twist", "def-sc-invertible-module", "lem-pc-projective-space-twist-cohomology"]
+++
Let $A$ be a commutative ring, $n\ge1$, and $P=\mathbf P^n_A$ with
standard opens $U_i=D_+(x_i)=\operatorname{Spec}R_i$, where
$R_i=A[x_k/x_i:k\ne i]$ is a polynomial ring in $n$ variables
([def-pc-proj]). Let $\Omega^1_{P/A}$ be the sheaf of relative
differentials: the $\mathcal O_P$-module whose restriction to $U_i$ is
associated with the module $\Omega^1_{R_i/A}$ of Kähler differentials,
glued along the canonical isomorphisms
$\Omega^1_{R_i/A}\otimes_{R_i}R_{ij}\cong\Omega^1_{R_{ij}/A}\cong
\Omega^1_{R_j/A}\otimes_{R_j}R_{ij}$, where
$R_{ij}=\Gamma(U_i\cap U_j,\mathcal O_P)$ is a localization of both
$R_i$ and $R_j$. Put
$\omega_P:=\Lambda^n\Omega^1_{P/A}$ and, on $U_i$,

$$
\eta_i:=(-1)^i\bigwedge_{k\ne i}d(x_k/x_i)
$$

(wedge over $k\in\{0,\ldots,n\}\smallsetminus\{i\}$ in increasing
order). Then $\Omega^1_{P/A}$ is locally free of rank $n$, $\omega_P$ is
an invertible module ([def-sc-invertible-module]) with basis $\eta_i$
on $U_i$, and there is an isomorphism

$$
\omega_P\;\xrightarrow{\ \sim\ }\;\mathcal O_P(-n-1)
$$

onto the twist of [def-pc-projective-space-twist], sending $\eta_i$ to
$e_i^{(-n-1)}$ on each $U_i$. In particular
$H^n(P,\omega_P)\cong A$
([lem-pc-projective-space-twist-cohomology] (ii)). For $n=1$ and
$A=k$, with $t=x_1/x_0$ and $s=x_0/x_1$, this is
$\omega_{\mathbf P^1}\cong\mathcal O(-2)$ with $\eta_0=dt$,
$\eta_1=-ds$ and $dt=-t^2ds$.
