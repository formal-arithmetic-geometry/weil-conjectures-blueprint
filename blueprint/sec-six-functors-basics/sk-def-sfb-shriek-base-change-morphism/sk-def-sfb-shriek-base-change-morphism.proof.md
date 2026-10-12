+++
kind  = "proof"
of    = "sk-def-sfb-shriek-base-change-morphism"
+++
We check that $c'$ is a compactification of $f'$ and that both squares are cartesian. The right
square is cartesian by the definition of $Z'$. The morphism $i'\colon X'\to Z'$ is well defined
because $p\circ i\circ g'=f\circ g'=g\circ f'$, and $p'\circ i'=f'$. The outer rectangle

$$
X'\xrightarrow{g'}X,\quad X'\xrightarrow{f'}Y',\quad X\xrightarrow{f=p\circ i}Y,\quad Y'\xrightarrow{g}Y
$$

is cartesian by hypothesis, and the right square is cartesian. By the pasting law for pullbacks,
the left square is cartesian too. Hence $i'$ is the base change of the open immersion $i$ along
$\bar g$, and so it is an open immersion. Likewise $p'$ is the base change of the proper morphism
$p$ along $g$, and so it is proper. This is the base change of compactifications of
[sk-prop-nagata-sketch-comp-category]. The scheme $Z'$ is separated and of finite type over
$k$, since $p'$ is proper and $Y'$ is separated and of finite type over $k$. So both squares lie in
the setting. The extension-by-zero exchange morphism of the left square is invertible by
[sk-def-sfb-open-base-change], which makes the second arrow well defined.
