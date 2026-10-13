+++
kind = "proof"
of = "pur7710-lem-basis-detection"
uses = ["pur7710-lem-derived-sections-bounded-below"]
+++
Let $C$ be a cone of $a$; it is bounded below, and $R\Gamma_{B,\Proet,\mathcal O_E/\varpi^n}(Lu^*_{B,\mathcal O_E/\varpi^n}C)=0$ for every test object, since $Lu^*_B$ and $R\Gamma_B$ are exact functors of triangulated categories. Suppose $C\neq0$, and let $m$ be the least degree with $\mathcal H^m(C)\neq0$. Since $Lu^*_{B,\mathcal O_E/\varpi^n}$ is levelwise and exact (Lemma “The finite-coefficient derived inverse image is levelwise” (`pur713-lem-finite-pull-levelwise`)), $Lu^*_BC$ has no cohomology below $m$ and $\mathcal H^m(Lu^*_BC)=u^*_B\mathcal H^m(C)$. Applying $R\Gamma_B$ to the truncation triangle $\mathcal H^m(Lu^*_BC)[-m]\to Lu^*_BC\to\tau^{\geq m+1}Lu^*_BC$ and using Lemma [pur7710-lem-derived-sections-bounded-below] for the third term gives
$0=H^mR\Gamma_{B,\Proet,\mathcal O_E/\varpi^n}(Lu^*_BC)=\Gamma(B_{\Proet},u^*_B\mathcal H^m(C))$.
For the weakly étale $u_B$, the latter is the group of sections of $\mathcal H^m(C)$ over the object $B$ of $W_{\Proet}$ (Input “Inverse image along a weakly étale morphism” (`pur713-input-fixed-weakly-etale`)). By Input [pur7710-input-ind-etale-basis] and the sheaf axiom, a sheaf with zero sections on all test objects has zero sections on every object; so $\mathcal H^m(C)=0$, a contradiction. The argument uses a least nonzero degree and is asserted only for bounded-below complexes.
