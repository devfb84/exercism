/*
 * space_age.h
 *
 *  Created on: Jun 17, 2019
 *      Author: felipe
 */

#ifndef SPACE_AGE_H_
#define SPACE_AGE_H_

namespace space_age
{

class space_age
{
public:
	space_age(long long secondsOld);
	virtual ~space_age();

	long long seconds() const;
	double on_earth() const;

private:
	long long secondsOld;

};
}



#endif /* SPACE_AGE_H_ */
