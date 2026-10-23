+++
kind  = "proof"
of    = "sk-i-dl-a1-local"
+++
Let $i:Z\hookrightarrow C$ be the inclusion of the whole finite
complement, and put $A(F)=i^*Rj_*F$. For a lisse sheaf $G$ on $U$, the
adjunction $j^*\dashv Rj_*$ shows that $i^!Rj_*G=0$, and applying
$i^!$ to the localization triangle ([sk-prop-sf-open-closed-triangle],
with $i^!i_*\simeq\mathrm{id}$ by [sk-prop-sf-closed-unit])
for $Rj_*G$ we obtain $i^!j_!G\simeq i^*Rj_*G[-1]$.
By Verdier exchange ([sk-thm-sf-verdier-exchange]) and duality on the
smooth curve ([sk-thm-pd-verdier-duality], with
$\mathbb D_UF=F^\vee(1)[2]$ by [sk-thm-purity-transport]), it follows
that

$$
 \begin{split}
 \mathbb D_Z A(F)
 &\simeq i^!\mathbb D_C Rj_*F
  \simeq i^!j_!\mathbb D_UF\\
 &\simeq i^*Rj_*(F^\vee(1)[2])[-1]
  =A(F^\vee)(1)[1].
 \end{split}
$$

On the finite geometric scheme $Z$, Verdier duality is the exact
duality of coefficient vector spaces. Taking degree $-1$ at $\bar s$,
we get $(R^1j_*F)_{\bar s}^\vee=(j_*F^\vee)_{\bar s}(1)$, which
is the pairing. It is Frobenius-equivariant because the adjunction,
localization and duality maps are natural in $F$ and respect its Weil
structure.
