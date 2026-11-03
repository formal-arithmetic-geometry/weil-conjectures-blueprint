+++
kind  = "proof"
of    = "lem-weil-pbc-comparison-global-cohomology"
+++
Since $\nu_T^*$ is exact by
[prop-weil-pbc-site-comparison-finite-level], its right adjoint $\nu_{T,*}$
in [def-weil-pbc-site-comparison-morphism] preserves injectives. For an
injective pro-etale resolution $J^\bullet$ of a bounded-below complex,
$\nu_{T,*}J^\bullet$ therefore computes its derived direct image and the
subsequent derived sections. Underived evaluation on the final object gives
$\Gamma(T_{\Et},\nu_{T,*}J^r)=\Gamma(T_{\Proet},J^r)$. Thus
$R\Gamma_{\Et}R\nu_{T,*}=R\Gamma_{\Proet}$. Apply this identity to the
derived unit, which is an isomorphism by [thm-weil-pbc-site-comparison].
