+++
kind = "proof"
of = "pur7710-lem-compact-interval"
uses = ["pur7710-lem-derived-sections-bounded-below"]
+++
Induct on the number of nonzero cohomology sheaves of $L$, using the truncation triangles and the long exact cohomology sequence of the exact functor $Rf_{!,\Et,\mathcal O_E/\varpi^n}$. For $L=F[-q]$ with $F$ a sheaf and $q\in[a,b]$, $\mathcal H^p(Rf_{!,\Et,\mathcal O_E/\varpi^n}F[-q])=\mathcal H^{p-q}(Rf_{!,\Et,\mathcal O_E/\varpi^n}F)$; it vanishes for $p-q<0$ because $\mathrm D(j_!)$ is exact and $p_*$ has no negative derived functors (Lemma [pur7710-lem-derived-sections-bounded-below] applied on the étale site, or the construction of Definition “Finite-coefficient étale derived direct image” (`pur456-pbc-pushforward`, see [sk-thm-sf-comp-composition]) on a resolution in degrees $\geq0$), and for $p-q>2e$ by Lemma [pur7710-lem-compact-amplitude]. Thus each such term lies in $[a,b+2e]$, and the long exact sequences keep the range.
