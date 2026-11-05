+++
kind = "proof"
of = "proposition-fourier-transform-perverse-heart--2"
order = 1260005
uses = ["proposition-fourier-transform-perverse-heart--1", "proposition-fourier-inversion", "lemma-perverse-sheaves-curve"]
+++
Put $F=\operatorname{FT}_\psi$. By
[proposition-fourier-transform-perverse-heart--1], $F$ and its inverse
preserve ${}^pD^{\le0}$ and ${}^pD^{\le-1}$. Fourier inversion then
shows that $F(K)$ satisfies the upper condition if and only if $K$
does.

For the lower condition use the orthogonality assertion of
Lemma [lemma-perverse-sheaves-curve]: a Weil complex $L$ lies in
${}^pD^{\ge0}$ if and only if every map $M\to L$, with
$M\in{}^pD^{\le-1}$, is zero. If $F(K)$ satisfies this condition,
apply $F$ to a map $M\to K$ and use faithfulness. Conversely, if $K$
satisfies it, transport a map $M\to F(K)$ through the counit
$F(F^{-1}M)\simeq M$ and fullness to a map $F^{-1}M\to K$.
Preservation of the upper class by $F^{-1}$ makes that map zero.
Combining the two conditions gives the equivalence.
