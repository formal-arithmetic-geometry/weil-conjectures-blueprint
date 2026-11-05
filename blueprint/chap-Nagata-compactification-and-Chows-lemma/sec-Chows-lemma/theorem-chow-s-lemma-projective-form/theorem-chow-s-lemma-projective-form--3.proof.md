+++
kind = "proof"
of = "theorem-chow-s-lemma-projective-form--3"
order = 1471006
uses = ["lemma-schematic-closure-uniqueness--1", "lemma-uniqueness-maps-dense-open--1"]
+++
Embed $X$ as a closed subscheme of a separated scheme $Y$ of finite
presentation over $S$. Apply Noetherian approximation to $S$ and
descend $Y\to S$ to a separated morphism $Y_0\to S_0$ of finite
presentation over a Noetherian scheme $S_0$, as in the proof of
Theorem [theorem-nagata-s-compactification-theorem]. The Noetherian
Chow construction, using [lemma-schematic-closure-uniqueness] and
[lemma-uniqueness-maps-dense-open], supplies a proper surjection
$Y'_0\to Y_0$ and an immersion of $Y'_0$ into a projective space over
$S_0$.

Pull back this diagram to $S$ and then to the closed subscheme $X$ of
$Y$. Properness and surjectivity are preserved. The cartesian square
for projective space identifies the base-changed immersion, and its
restriction to the inverse image of $X$ is still an immersion. Its
composite with the projection is $f\pi$.

The Noetherian construction uses a projective space whose homogeneous
coordinates are indexed by a finite set. A linear closed immersion puts
this space inside $\mathbf P^n_S$ for some $n\geq 0$. Composing with it
gives the assertion.

If $f$ is proper, then $q_Si_S=f\pi$ is proper. Since $q_S$ is
separated, $i_S$ is proper, hence a proper immersion and therefore a
closed immersion. This recovers the closed immersion of
[theorem-chow-s-lemma-projective-form--1] over a general qcqs base.
