+++
kind  = "proof"
of    = "def-sfb-modobj-restrict-coextend-adjunction"
+++
We use elementwise notation for morphisms out of tensor products, as in
[def-sfb-modobj-coextension]. Identities between maps into
$\Hom_{\mathcal R}(\mathcal S,N)$ are checked after evaluation.
- $\varepsilon_N$ is $\mathcal R$-linear for the restricted action
  ([def-sfb-modobj-restriction]): $(\varphi(r)\cdot g)(1)=g(\varphi(r))=r\cdot g(1)$, by the
  equalizer condition.
- Let $f\colon\operatorname{Res}_\varphi M\to N$ be $\mathcal R$-linear. The map
  $s\mapsto f(sm)$ lies in $\Hom_{\mathcal R}(\mathcal S,N)$, because
  $f(\varphi(r)sm)=r\cdot f(sm)$ by linearity of $f$. The assignment
  $m\mapsto(s\mapsto f(sm))$ is $\mathcal S$-linear, because
  $s\mapsto f(ss'm)$ is $s'\cdot(s\mapsto f(sm))$.
- The two constructions are mutually inverse by the unit law of $\mathcal S$. Naturality
  is immediate.
