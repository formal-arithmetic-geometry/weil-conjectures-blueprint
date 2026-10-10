+++
kind  = "proof"
of    = "sbc-lem-bc-injectivity"
+++
Choose a short exact sequence
$0\to\mathcal F\to\mathcal I\to\mathcal Q\to0$ with $\mathcal I$ an
injective sheaf of $\mathbf Z/n\mathbf Z$-modules on $T_{\Et}$. The
injective-acyclicity input of [lemma-weil-pbc-leray-acyclicity]
(using the adjunction of [def-weil-pbc-inverse-image]) gives
$R^qg_*\mathcal I=0$ for $q>0$, so the two long exact sequences of
higher direct images of [def-weil-pbc-direct-image] (in the
derived categories of [def-weil-pbc-derived-categories], the
distinguished triangle of the short exact sequence) and the naturality
of the base-change maps of [sbc-def-base-change-map] ([sbc-lem-bc-naturality]) give the
diagram with exact rows of the statement: the long exact sequences are
the ones of [lemma-weil-pbc-five-lemma-transfer]; the left two
vertical arrows are the degree-$(q-1)$ base-change maps for
$\mathcal I$ and $\mathcal Q$ for the base change $f'$ along $g$, hence
isomorphisms by $\mathrm{BC}(f',n,q-1)$, which is part of the
hypothesis that $\mathrm{BC}(f,n,q-1)$ holds universally (only this
single degree enters), the top
right entry $f'^{-1}R^qg_*\mathcal I$ is zero, hence the middle vertical arrow is injective,
which is (1), and the same diagram gives the inclusion of the cokernel
into $R^qh_*e^{-1}\mathcal I$, which is (3); for (2), with
$\mathcal F\subset\mathcal G\subset\mathcal I$, the same diagram
applied to $\mathcal F\subset\mathcal G$ gives the inclusion of the
cokernels.
