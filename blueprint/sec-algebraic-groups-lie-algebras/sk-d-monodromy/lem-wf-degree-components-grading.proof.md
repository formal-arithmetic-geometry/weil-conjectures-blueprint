+++
kind  = "proof"
of    = "lem-wf-degree-components-grading"
+++
By [lem-wf-arith-extension-group] the displayed multiplication of
[def-wf-arithmetic-monodromy-extension] makes
$G_{\mathrm{arith}}(\rho)$ a group whose degree map $\deg_G$ is a
homomorphism, and $G^{[m]}=\deg_G^{-1}(m)$ by
[def-wf-degree-components]. Hence the product of an element of
$G^{[m]}$ with one of $G^{[n]}$ has degree $m+n$ and so lies in
$G^{[m+n]}$, while conversely every $(h,m+n)\in G^{[m+n]}$ equals
$(h,m)(1,n)$ with $(h,m)\in G^{[m]}$ and $(1,n)\in G^{[n]}$; this
gives the first identity. Inversion preserves the degree by the same
homomorphism property, so $(G^{[m]})^{-1}\subseteq G^{[-m]}$, and
applying this containment with $-m$ in place of $m$ and taking
inverses gives the reverse containment.
