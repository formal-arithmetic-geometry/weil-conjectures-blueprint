+++
id = "prose-06-12"
kind = "hidden"
title = "Construction of $Rf_!$"
order = 292
+++
From now on, $\Lambda$ is any admissible coefficient ring. What we need
from Lemmas [sk-lem-proper-heart-bound] and [sk-lem-proper-unbounded-window]
is that $Rp_*$ preserves direct sums for proper $p$; for the other
coefficient rings this is proved separately, as recalled in the next proof.

Two things remain. The functor $Rp_*\circ j_!$ should not depend on the
compactification, and it should be compatible with composition and base
change. All of this follows from proper base change, and the mechanism is
the same each time. The comparison maps are maps out of an extension by
zero $j_!K$, so they are determined by their restriction to $X$, where
they are the identity. To see that such a map is an isomorphism, we
restrict it to the closed complement of $X$, where proper base change
shows that both sides vanish. For instance, if $h:Z'\to Z$ is proper and
$h^{-1}(X)=X$, then $Rh_*j'_!K$ restricted to $Z\setminus X$ is the direct
image of the restriction of $j'_!K$ to $Z'\setminus X$, which is zero.
Since proper base change is only known on $D^b_{\mathrm{ctf}}$, we first show that all
the functors involved preserve direct sums, so that it suffices to check
isomorphisms on $D^b_{\mathrm{ctf}}$ (Lemma [sk-lem-sf-determination]).

We first show that both factors of $Rp_*\circ j_!$ preserve the localizing
categories. For this we use the definition of $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ in the following
form: if the objects of $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ with some property form
a triangulated subcategory that is closed under direct sums and contains
$D^b_{\mathrm{ctf}}(X,\Lambda)$, then every object of $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ has the
property.
