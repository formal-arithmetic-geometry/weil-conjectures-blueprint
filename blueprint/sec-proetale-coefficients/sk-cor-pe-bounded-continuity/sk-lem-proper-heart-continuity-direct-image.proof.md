+++
kind = "proof"
of = "det-proper-heart-continuity-direct-image"
+++
Let $V\to Y$ be an affine weakly contractible object and $X_V=X\times_YV$, which is qcqs because $V$ is
affine and $p$ is qcqs. $R^qp_*M$ is the sheaf associated to $V'\mapsto H^q(X_{V'},M)$. Since $\Gamma(V,-)$
is exact ([det-proper-heart-continuity-sections]), applying it to a K-injective resolution gives

$$
(R^qp_*M)(V)=H^q\bigl(\Gamma(V,Rp_*M)\bigr)=H^q(R\Gamma(X_V,M|_{X_V}))=H^q((X_V)_{\mathrm{proét}},M|_{X_V}).
$$

Restriction to $X_V$ commutes with colimits (it has a right adjoint). Hence, for a filtered diagram
$(M_i)$, the comparison $\varinjlim R^qp_*M_i\to R^qp_*\varinjlim M_i$ evaluated on $V$ is (using that
$\Gamma(V,-)$ preserves colimits, [det-proper-heart-continuity-sections])

$$
\varinjlim_iH^q(X_V,M_i|_{X_V})\to H^q(X_V,\varinjlim_iM_i|_{X_V}),
$$

an isomorphism by [det-proper-heart-continuity-cohomology] for $Z=X_V$. Affine weakly contractible
objects form a basis of the site, and evaluation on them detects isomorphisms of sheaves
([sk-cor-pe-sections]). The case of direct sums is identical.
