+++
kind  = "proof"
of    = "sk-rem-sf-kv-formal"
uses = ["sk-prop-sf-biduality-general", "sk-thm-sf-verdier-exchange", "sk-thm-sf-dual-perfect", "sk-prop-sf-dualizable-biduality"]
+++
By biduality [sk-prop-sf-biduality-general], $\mathbb D$ is an
anti-equivalence of $\Dctf$ with $\mathbb D\mathbb D\cong\mathrm{id}$. So the
Verdier exchange $\mathbb D_XRf^!\cong Lf^*\mathbb D_Y$ of
[sk-thm-sf-verdier-exchange] can be rewritten as
$Rf^!\cong\mathbb D_XLf^*\mathbb D_Y$. Apply this to $p_X$, and use the
internal adjunction $\RHom(A,\mathbb DC)\cong\mathbb D(A\otimes^LC)$ with
$A=p_Y^*N$ and $C=p_X^*\mathbb D_XM$:

$$
\RHom(p_Y^*N,Rp_X^!M)\cong\RHom(p_Y^*N,\mathbb D_{X\times Y}p_X^*\mathbb D_XM)
\cong\mathbb D_{X\times Y}(\mathbb D_XM\boxtimes N).
$$

Each step is natural, so $\kappa_{M,N}$ is an isomorphism exactly when the
map $\mathbb D_XM\boxtimes\mathbb D_YN\to\mathbb D_{X\times Y}(M\boxtimes N)$
is one (substitute $\mathbb D_XM$ for $M$ and use biduality once more). For
perfect $M,N$ on smooth $X,Y$ of pure dimension, [sk-thm-sf-dual-perfect]
gives $\mathbb D M\cong M^\vee(d)[2d]$. Duals of dualizable objects commute
with $\boxtimes$ ([sk-prop-sf-dualizable-biduality]), so that case is formal.
