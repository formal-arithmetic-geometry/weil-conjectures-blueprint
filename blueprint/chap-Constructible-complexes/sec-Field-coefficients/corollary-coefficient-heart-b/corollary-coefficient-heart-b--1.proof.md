+++
kind = "proof"
of = "corollary-coefficient-heart-b--1"
order = 273003
uses = ["definition-lisse-sheaves", "lemma-inverse-image-coefficient-sheaves--1", "definition-constructible-sheaves--1", "definition-constructible-sheaves--2", "definition-constructible-sheaves--3", "definition-constructible-sheaves--5", "definition-constructible-sheaves--6", "lemma-constructible-sheaves--3"]
+++
The first assertion is closure under cones, which we check on cohomology sheaves.
Let $K\to K'\to K''\to K[1]$ be a distinguished triangle with $K,K'$ in
$\Dbc(X,\Lambda)$. By the long exact cohomology sequence, each
$\mathcal H^i(K'')$ is an extension of
$\ker(\mathcal H^{i+1}K\to\mathcal H^{i+1}K')$ by
$\coker(\mathcal H^iK\to\mathcal H^iK')$. Both are constructible by
Lemma [lemma-constructible-sheaves](1), and hence so is $\mathcal H^i(K'')$.
Closure under shifts is clear, since shifts only renumber the cohomology sheaves.

*Source:* the proof of Corollary [corollary-coefficient-heart-b].
