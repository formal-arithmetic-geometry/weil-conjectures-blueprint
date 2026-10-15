+++
kind = "proof"
of = "det-proper-unbounded-window-ii-bounded"
+++
The comparison map is adjoint to the sum of the maps $Rp_*M_\alpha\to Rp_*\bigoplus M_\alpha$ induced by the
inclusions. Induction on $b-a$.

*$a=b$.* $M_\alpha\cong B_\alpha[-a]$ with $B_\alpha\in\IndCons(X,\Lambda)$ and
$\bigoplus M_\alpha\cong(\bigoplus B_\alpha)[-a]$. Since cohomology commutes with direct sums of complexes of
sheaves, $\mathcal H^{n}$ of the comparison map is $\bigoplus_\alpha R^{n+a}p_*B_\alpha\to R^{n+a}p_*\bigoplus B_\alpha$,
an isomorphism by [sk-lem-proper-heart-bound]. A map in the derived category inducing isomorphisms on all
cohomology sheaves is an isomorphism.

*Induction step.* The truncation triangles $\tau_{\leq b-1}M_\alpha\to M_\alpha\to\mathcal H^b(M_\alpha)[-b]\to$
sum to the truncation triangle of $\bigoplus M_\alpha$ (cohomology commutes with sums,
[sk-cor-ambient-ind-derived]). Applying $Rp_*$, and using that a sum of distinguished triangles is
distinguished, the comparison maps form a morphism of triangles

$$
\Bigl(\bigoplus Rp_*\tau_{\leq b-1}M_\alpha\to\bigoplus Rp_*M_\alpha\to\bigoplus Rp_*\mathcal H^b(M_\alpha)[-b]\to\Bigr)
\longrightarrow
\Bigl(Rp_*\textstyle\bigoplus\tau_{\leq b-1}M_\alpha\to Rp_*\bigoplus M_\alpha\to Rp_*\bigoplus\mathcal H^b(M_\alpha)[-b]\to\Bigr),
$$

whose outer components are isomorphisms by induction. On cohomology sheaves the five lemma shows the
middle component induces isomorphisms, hence is an isomorphism.
