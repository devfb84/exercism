#include "space_age.h"

namespace space_age
{

space_age::space_age(long long secondsOld):secondsOld(secondsOld)
{
}

space_age::~space_age()
{
}

long long space_age::seconds() const
{
	return secondsOld;
}

double space_age::on_earth() const
{
	return secondsOld / 31557600;
}

}

