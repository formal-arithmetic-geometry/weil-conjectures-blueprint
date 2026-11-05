+++
kind = "proof"
of = "lemma-local-duality-point-c-u"
order = 1292
uses = ["proposition-etale-implications", "lemma-stability", "proposition-pro-etale-coverings", "proposition-pro-etale-affines-form-basis", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection"]
+++
The two stalks are cohomology sheaves of the complexes $i^*Rj_*F^\vee$
(in degree zero) and $i^*Rj_*F$ (in degree one) on the boundary. We
compute the Verdier dual of the second complex by duality on the curve,
and we find the first one, shifted and twisted.

Let $i:Z\hookrightarrow C$ be the inclusion of the whole finite
complement, and put $K_F=i^*Rj_*F$. For a lisse sheaf $G$ on $U$, the
adjunction $j^*\dashv Rj_*$ shows that $i^!Rj_*G=0$, and applying
$i^!$ to the localization triangle for $Rj_*G$ we obtain
$i^!j_!G\simeq i^*Rj_*G[-1]$. Since duality
exchanges $Rj_*$ with $j_!$ and $i^*$ with $i^!$, this formula lets us
write the result again in the form $i^*Rj_*$. Indeed, by Verdier duality on
the smooth curve, $\mathbb D_UF=F^\vee(1)[2]$ for the lisse sheaf $F$,
and we find

$$
\begin{split}
\mathbb D_Z K_F
&\simeq i^!\mathbb D_C Rj_*F
\simeq i^!j_!\mathbb D_UF\\
&\simeq i^*Rj_*(F^\vee(1)[2])[-1]
=K_{F^\vee}(1)[1].
\end{split}
$$

On the finite geometric scheme $Z$, Verdier duality is the exact
duality of coefficient vector spaces, so taking degree $-1$ at $\bar s$
we get $(R^1j_*F)_{\bar s}^\vee=(j_*F^\vee)_{\bar s}(1)$, which
is the pairing. It is Frobenius-equivariant because the adjunction,
localization and duality maps are natural in $F$ and respect its Weil
structure.
