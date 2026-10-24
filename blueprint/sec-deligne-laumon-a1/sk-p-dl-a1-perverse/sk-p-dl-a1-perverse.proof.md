+++
kind  = "proof"
of    = "sk-p-dl-a1-perverse"
+++
Everything happens on Weil complexes. For $n\in\mathbf Z$ write
${}^pD^{\le n}={}^pD^{\le0}[-n]$: the Weil complexes $K$ with
$\mathcal H^aK=0$ for $a>n$ and $\mathcal H^nK$ of finite support.
These conditions are invariant under isomorphism and under Tate
twists, which change neither the vanishing nor the support of a
cohomology Weil sheaf. By [sk-thm-inversion], $\operatorname{FT}_\psi$
is an equivalence with quasi-inverse
$\operatorname{FT}_{\psi^{-1}}(-)(1)$.

*The upper classes.* We first show two facts about the transform.

(a) A sheaf of finite support placed in degree $n$ transforms into a
complex concentrated in degrees $\le n-1$. Indeed, by the stalk formula
of [sk-thm-inversion] the transform of a geometric skyscraper is a
lisse sheaf shifted by one.

(b) If $\mathcal H^aK=0$ for $a>m$, then $\mathcal H^a$ of the
transform vanishes for $a>m+1$, and its $\mathcal H^{m+1}$ has finite
support. By the stalk formula and [sk-l-dl-a1-endpoints], the stalk of
the transform at a closed geometric point $y$ is the compact-support
cohomology of $K\otimes\mathcal L_{\psi(yx)}$ shifted by one, with
each cohomology sheaf contributing in degrees $0,1,2$ only. This gives
the bound, and the top stalk is

$$
 H_c^2(\mathbf A^1,\mathcal H^mK\otimes\mathcal L_{\psi(yx)}).
$$

On a dense open where $\mathcal H^mK$ is lisse with generic
representation $V$, this is $(V\otimes\chi_y)_{\pi_1}(-1)$, which is
nonzero only if $V$ has the rank-one quotient $\chi_y^{-1}$.
The characters $\chi_y$ are pairwise distinct. Indeed, the quotient
of two of them is the character of a nonzero linear function, whose
cohomology vanishes by [sk-lem-wft-character-integral], whereas a
trivial character has nonzero top compact-support cohomology; and a
character trivial on the dense open is trivial on the line, by the
surjectivity of fundamental groups. Since the map from $V$ onto a sum
of pairwise nonisomorphic simple characters is surjective, $V$ has at
most $\dim V$ such distinct quotients. Thus the top cohomology Weil
sheaf has only finitely many nonzero closed geometric stalks. Being
constructible, it has finite support.

Now let $K\in{}^pD^{\le n}$, and apply the transform to the truncation
triangle

$$
 \tau^{<n}K\to K\to\mathcal H^nK[-n]\to.
$$

By (a), the transform of the third vertex has no cohomology in degrees
$\ge n$, so the long exact sequence of cohomology Weil sheaves makes
$\mathcal H^a\operatorname{FT}_\psi(\tau^{<n}K)\to
\mathcal H^a\operatorname{FT}_\psi(K)$ surjective for $a\ge n$. By (b)
with $m=n-1$, the source vanishes for $a>n$ and has finite support for
$a=n$. Hence $\operatorname{FT}_\psi$ preserves ${}^pD^{\le n}$. The
same argument applies to $\psi^{-1}$, and the Tate twist does not
change the classes, so the quasi-inverse
$\operatorname{FT}_{\psi^{-1}}(-)(1)$ also preserves every
${}^pD^{\le n}$.

*The lower class.* By [sk-lem-wft-curve-heart], ${}^pD^{\ge0}$ is the
right orthogonal of ${}^pD^{\le-1}$. Write $F=\operatorname{FT}_\psi$
and $G=\operatorname{FT}_{\psi^{-1}}(-)(1)$, and let
$M\in{}^pD^{\le-1}$. If $K\in{}^pD^{\ge0}$, then

$$
 \operatorname{Hom}(M,FK)\cong\operatorname{Hom}(GM,K)=0,
$$

since $GM\in{}^pD^{\le-1}$; so $FK\in{}^pD^{\ge0}$. Conversely, if
$FK\in{}^pD^{\ge0}$, then
$\operatorname{Hom}(M,K)\cong\operatorname{Hom}(FM,FK)=0$, since $F$ is
fully faithful and $FM\in{}^pD^{\le-1}$; so $K\in{}^pD^{\ge0}$. The
same holds for $G$. Hence $F$ and $G$ are t-exact, and a Weil complex
is a perverse Weil sheaf exactly when its transform is.

*The hearts.* Consequently $F$ and $G$ restrict to quasi-inverse
functors between the perverse Weil hearts. They are exact, since a
short exact sequence of the heart is a distinguished triangle with all
three vertices in the heart, and $F$ and $G$ are triangulated. An
equivalence of categories preserves simple objects.
