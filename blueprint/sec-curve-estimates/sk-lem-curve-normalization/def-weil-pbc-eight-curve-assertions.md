+++
id = "def-weil-pbc-eight-curve-assertions"
kind = "definition"
title = "The eight curve-cohomology assertions"
lean = ["AlgebraicGeometry.IsCurve.Assertions", "AlgebraicGeometry.IsCurve.assertions_iff"]
order = 1474
uses = ["def-weil-pbc-C1", "def-weil-pbc-C2", "def-weil-pbc-C3", "def-weil-pbc-C4", "def-weil-pbc-C5", "def-weil-pbc-C6", "def-weil-pbc-C7", "def-weil-pbc-C8", "def-weil-pbc-curve-setting"]
+++
For a curve coefficient pair [def-weil-pbc-curve-setting] $(C,F)$ (so $k$ is
algebraically closed, $C$ is separated of finite type over $k$ with
$\dim C\leq1$, and $F$ is a torsion sheaf on $C_{\Et}$), write
$\mathcal C(C,F)$ for the conjunction of the eight assertions

$$
 \mathcal C(C,F)=\bigwedge_{j=1}^{8}\mathcal C_j(C,F),
$$

namely:

1. [def-weil-pbc-C1]: $H^q(C_{\Et},F)=0$ for $q>2$;
1. [def-weil-pbc-C2]: $H^q(C_{\Et},F)=0$ for $q>1$ when $C$ is affine;
1. [def-weil-pbc-C3]: $H^q(C_{\Et},F)=0$ for $q>1$ when $\operatorname{char}k=p>0$ and $F$ is
$p$-primary;
1. [def-weil-pbc-C4]: every $H^q(C_{\Et},F)$ is finite when $F$ is constructible and prime
to $\operatorname{char}k$;
1. [def-weil-pbc-C5]: every $H^q(C_{\Et},F)$ is finite when $C$ is proper and $F$ is
constructible;
1. [def-weil-pbc-C6]: for every algebraically closed extension $k'/k$, the pullback map
$H^q(C_{\Et},F)\to H^q((C_{k'})_{\Et},F_{k'})$ is an isomorphism when $F$ is
prime to $\operatorname{char}k$;
1. [def-weil-pbc-C7]: the map in (6) is an isomorphism when $C$ is proper, without a
restriction on the torsion;
1. [def-weil-pbc-C8]: for every open immersion $a:U\hookrightarrow C$, the restriction
$H^2(C_{\Et},F)\to H^2(U_{\Et},a^{-1}F)$ is surjective.
