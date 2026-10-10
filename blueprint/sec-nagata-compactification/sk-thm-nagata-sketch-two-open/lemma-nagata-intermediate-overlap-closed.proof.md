+++
kind  = "proof"
of    = "lemma-nagata-intermediate-overlap-closed"
uses = ["lemma-nagata-proper-extension-graph-closed"]
+++
By [lemma-nagata-intermediate-overlap-constructible], the image is
constructible. By
[lemma-nagata-intermediate-overlap-specialization-closed], it is stable
under specialization. The target is Noetherian, so the image is closed.
Factor the given immersion as a closed immersion into an open subscheme
$T'\subseteq T$, where
$T=U\times_S(X_i\setminus\overline Z_{i,j})$. Over $T'$ the map is a
closed immersion by construction. Over the open complement of its closed
image in $T$, its inverse image is empty, hence is also a closed immersion.
These two opens cover $T$: every point outside $T'$ is outside the image.
Since being a closed immersion is local on the target, the original
immersion is a closed immersion.
