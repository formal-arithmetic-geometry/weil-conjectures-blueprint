+++
kind = "proof"
of = "det-pe-constructible-comparison-equivalence"
+++
*(1).* Let $G$ be a constructible étale sheaf, with (locally on $X$) a partition
into constructible locally closed strata $Z$ on which $G|_Z$ is étale locally
constant of finite type. For the immersion $i\colon Z\to X$,
[lem-weil-pbc-comparison-pullback] gives $i^*\nu_X^*G\cong\nu_Z^*i^*G$, and
$\nu_Z^*$ carries a local system of finite type to a pro-étale one (an étale
covering is a pro-étale covering and constant sheaves go to constant sheaves).
So $\nu_X^*G$ is constructible. The functor $\nu_X^*$ is fully faithful on module
sheaves ([det-pe-classical-sheaves-modules]). Conversely let $F$ be
constructible on $X_{\Proet}$. By [det-pe-constructible-comparison-classical] it is
classical, so $F\cong\nu_X^*G$ with $G=\nu_{X,*}F$. For a stratum $Z$ as above,
$\nu_Z^*i^*G\cong i^*F$ is a pro-étale local system of finite type, so by
[det-pe-finite-local-systems-twist] it is $\cong\nu_Z^*H$ for an étale local system
$H$ of finite type, and full faithfulness of $\nu_Z^*$ gives $i^*G\cong H$. Hence
$G$ is constructible, and $\nu_X^*$ is essentially surjective onto
$\operatorname{Cons}(X,\Lambda)$.

*(2).* For $L\in D^b_c(X_{\Et},\Lambda)$, exactness gives
$H^q(\nu_X^*L)\cong\nu_X^*H^q(L)$, constructible by (1) and zero for all but
finitely many $q$; so $\nu_X^*L\in\Dbc(X,\Lambda)$. Full faithfulness on
$D^+$ is the unit isomorphism of [det-pe-classical-derived-equivalence]. For
$K\in\Dbc(X,\Lambda)$, every $H^q(K)$ is constructible, hence classical by
[det-pe-constructible-comparison-classical], so
$K\in D^+_{\mathrm{class}}(X_{\Proet},\Lambda)$ and $K\cong\nu_X^*L$ with
$L=R\nu_{X,*}K\in D^+(X_{\Et},\Lambda)$. Then
$\nu_X^*H^q(L)\cong H^q(K)$; as $\nu_X^*$ is fully faithful and exact,
$H^q(L)\cong\nu_{X,*}H^q(K)$ is constructible by (1) and vanishes whenever
$H^q(K)=0$. So $L\in D^b_c(X_{\Et},\Lambda)$, and $\nu_X^*$ is essentially
surjective. It is exact, hence a triangulated equivalence.
