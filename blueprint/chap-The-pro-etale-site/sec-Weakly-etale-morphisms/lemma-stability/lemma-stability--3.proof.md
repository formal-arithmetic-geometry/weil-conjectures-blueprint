+++
kind = "proof"
of = "lemma-stability--3"
order = 32011
+++
Flatness of $f$ is local on its source. For the diagonal condition,
the restriction of $\Delta_{U/X}$ to $U_i$ is the composite
$$
U_i\longrightarrow U_i\times_XU_i\longrightarrow U\times_XU.
$$
The second map is an open immersion. Composing with an open immersion
preserves and reflects flatness, so this restriction is flat if and
only if $\Delta_{U_i/X}$ is flat. Apply locality of flatness to the
covering $U=\bigcup_iU_i$. Lean expresses this as locality of the
diagonal property, then combines it with locality of flatness of $f$.
