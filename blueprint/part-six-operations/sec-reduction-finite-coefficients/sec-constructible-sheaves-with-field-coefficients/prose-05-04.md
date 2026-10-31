+++
id = "prose-05-04"
kind = "hidden"
title = "Constructible sheaves with field coefficients"
order = 235
+++
Until the end of this subsection, $\Lambda=E$ or $\overline{\mathbf Q}_\ell$, so that
$D^b_{\mathrm{ctf}}=\Dbc$ and we can argue with constructible cohomology sheaves
and standard truncations. Recall (after
Definition [sk-def-sfb-constructible]) that a $\Lambda_X$-module is
constructible exactly when it is *lisse*, that is locally free of
finite rank for the pro-étale topology, on each stratum of a finite
stratification of $X$. By dévissage we reduce statements about
$\Dbc(X,\Lambda)$ to the simplest constructible sheaves, namely lisse sheaves
extended by zero from a stratum. For a general finite $A$, finite Tor
amplitude is a condition on the whole complex, and instead of this
dévissage through the heart we use the finite flat
models of Lemma [sk-lem-sf-flat-model].

For a locally closed immersion
$a:S\hookrightarrow X$, we factor $a=i\circ j$ with $j:S\hookrightarrow\overline S$ the open
immersion into the closure and $i:\overline S\hookrightarrow X$ the closed
immersion, and we put
$a_!=i_*j_!:\operatorname{Mod}(S_{\mathrm{pro}\acute{e}t},\Lambda)\to \operatorname{Mod}(X_{\mathrm{pro}\acute{e}t},\Lambda)$.
Since $j_!$ and $i_*$ are exact, so is $a_!$, and therefore it induces
$a_!:D(S_{\mathrm{pro}\acute{e}t},\Lambda)\to D(X_{\mathrm{pro}\acute{e}t},\Lambda)$ without deriving.

For this dévissage we need constructible sheaves to form an
abelian category (Lemma [sk-lem-coefficient-heart]). The proof reduces a
morphism of lisse $E$-sheaves to a morphism of integral lattices, and for
$\overline{\mathbf Q}_\ell$ descends it to a finite $E$; the next two lemmas provide the
lattices locally and the descent.
