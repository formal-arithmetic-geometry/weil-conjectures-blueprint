+++
kind = "proof"
of = "det-sp-constant-family-conservative"
uses = ["lemma-weil-pbc-geometric-stalk-conservative"]
+++
Give $T$ its reduced structure and let $u\colon T\hookrightarrow\bar Y$ be the inclusion. Since
$E$ is supported on $T$, the unit $E\to u_*u^*E$ is an isomorphism, so $Rq_*E\simeq R(qu)_*u^*E$,
and $qu$ is finite. Finite direct image is exact, so
$H^r(Rq_*E)\simeq(qu)_*H^r(u^*E)$ for every $r$. On a geometric stalk at $\bar b\to B$, the direct
image of a sheaf under the finite map $qu$ is the finite product of its stalks at the geometric
points of the finite fibre $T_{\bar b}$. A zero direct image therefore forces all stalks of every
$H^r(E)$ at points of $T$ to vanish; the stalks off $T$ vanish by the support hypothesis. Geometric
stalks detect isomorphisms of étale sheaves [lemma-weil-pbc-geometric-stalk-conservative], so every
$H^r(E)$ is zero and $E=0$.
