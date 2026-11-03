+++
kind  = "proof"
of    = "lemma-nagata-strict-chart-map-surjective"
uses = ["lemma-nagata-localization-ideal-pow", "lemma-nagata-rees-piece-membership"]
+++
By [lemma-nagata-chart-ring-normal-form], the target is generated as a
$B$-algebra by the fractions $z/b$ with $z\in J$. Write
$z=\sum_k y_k\overline{x_k}$ with $x_k\in I$. Then

$$
z/b=\sum_k\sigma_a\bigl(y_k\otimes(x_k/a)\bigr),
$$

proving surjectivity.
