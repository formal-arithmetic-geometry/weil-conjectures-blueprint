+++
kind  = "proof"
of    = "thm-pur-with-support-exactness"
+++
Step 1: the derived support object. For a bounded-below complex $F$ (a torsion sheaf placed in degree zero)
choose a bounded-below resolution $F\to I^{\bullet}$ whose terms are
injective sheaves ([Stacks, Tag 079P]). The complex of sections with
support in $Z$ is the kernel of the restriction
$\Gamma(X,I^{\bullet})\to\Gamma(U,I^{\bullet})$, and this
kernel is the complex computing $R\Gamma_Z(X,\cdot)$ by
[def-pur-support-cohomology]. Step 2: termwise exactness. For an
injective sheaf $I$ the restriction $\Gamma(X,I)\to\Gamma(U,I)$ is
surjective: it is the map
$\operatorname{Hom}(\mathbf Z_X,I)\to\operatorname{Hom}(j_!\mathbf Z_U,I)$
induced by the monomorphism $j_!\mathbf Z_U\to\mathbf Z_X$
([def-weil-open-closed-recollement]), and $\operatorname{Hom}(-,I)$ is
exact. Hence
$0\to\Gamma_Z(X,I^q)\to\Gamma(X,I^q)\to\Gamma(U,I^q)\to0$ is exact for
every $q$. Step 3: the long exact
sequence. The short exact sequence of complexes

$$
0\longrightarrow\Gamma_Z(X,I^{\bullet})
\longrightarrow\Gamma(X,I^{\bullet})
\longrightarrow\Gamma(U,I^{\bullet})\longrightarrow0
$$

(exact termwise by Step 2) gives, by the zig-zag/snake lemma applied to the exact sequence
of cochain complexes, the long exact sequence of cohomology

$$
\cdots\to H^q_Z(X,F)\to H^q(X,F)\to H^q(U,F)\to H^{q+1}_Z(X,F)\to\cdots,
$$

with the connecting morphism the one of the injective
resolution; the functoriality in the pair and in $F$ is the
functoriality of all the maps. Step 4: complexes and the pro-etale
site. For bounded-below complexes with torsion cohomology the same
argument runs with a bounded-below resolution by injective sheaves
([Stacks, Tag 079P]), Step 2 applying to each term, and the finite-torsion case
on the pro-etale site is the transport of the etale statement along
the site comparison [thm-weil-pbc-site-comparison] of the proper-base-change chapter (the sheaves being finite-torsion, the site comparison preserves
the support and the exactness).
