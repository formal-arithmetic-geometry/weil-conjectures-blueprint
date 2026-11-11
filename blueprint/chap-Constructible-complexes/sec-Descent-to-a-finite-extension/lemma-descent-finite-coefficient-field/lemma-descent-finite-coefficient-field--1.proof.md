+++
kind = "proof"
of = "lemma-descent-finite-coefficient-field--1"
order = 285004
+++
Morphisms descend because $\QbarX$ is the filtered colimit of the $E'_X$
and Hom out of a constructible complex commutes with this colimit
(Lemma [lemma-continuity-ext-out-constructible-complex]). Objects are built from
lisse sheaves by finitely many extensions, each classified by a
morphism, and so they descend as well.

(1) Extension of scalars $E'_X\otimes_{E_X}-$ is left adjoint to
restriction of scalars $D(X_{\mathrm{pro}\acute{e}t},E')\to D(X_{\mathrm{pro}\acute{e}t},E)$. Hence
$\Hom_{D(X_{\mathrm{pro}\acute{e}t},E')}(C_{E'},D_{E'}[r])=\Hom_{D(X_{\mathrm{pro}\acute{e}t},E)}(C,D_{E'}[r])$,
and similarly for $\overline{\mathbf Q}_\ell$. Represent $D$ by a bounded complex $D^\bullet$.
The complexes $D^\bullet\otimes_{E_X}E'_X$ form a filtered system of
complexes of $E_X$-modules, all vanishing below the lower bound of
$D^\bullet$. Their colimit is $D^\bullet\otimes_{E_X}\QbarX$, which
represents $D_{\overline{\mathbf Q}_\ell}$. Applying Lemma [lemma-continuity-ext-out-constructible-complex]
to $C\in\Dbc(X,E)$, we get

$$
\varinjlim_{E'}\Hom_{D(X_{\mathrm{pro}\acute{e}t},E)}(C,D_{E'}[r])
\xrightarrow{\ \sim\ }\Hom_{D(X_{\mathrm{pro}\acute{e}t},E)}(C,D_{\overline{\mathbf Q}_\ell}[r]),
$$

which is the claim after the adjunction.

*Source:* the proof of Lemma [lemma-descent-finite-coefficient-field].
